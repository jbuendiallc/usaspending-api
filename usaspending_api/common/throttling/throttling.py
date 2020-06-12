from rest_framework import throttling
from django.core.cache import cache as default_cache
import time
from rest_framework.settings import api_settings


class CustomRateThrottle(throttling.SimpleRateThrottle):

    #
    cache = default_cache
    timer = time.time
    cache_format = "throttle_%(scope)s_%(ident)s"
    scope = "custom"
    THROTTLE_RATES = api_settings.DEFAULT_THROTTLE_RATES
    keyword = "Token"
    model = None

    def get_cache_key(self, request, view):
        return self.cache_format % {"scope": self.scope, "ident": request.META.get("REMOTE_ADDR")}

    # THROTTLE_RATES = api_settings.DEFAULT_THROTTLE_RATES
    def allow_request(self, request, view):

        """
        Implement the check to see if the request should be throttled.

        On success calls `throttle_success`.
        On failure calls `throttle_failure`.
        """
        if request.headers.get("X-Requested-With") == "USASpendingFrontend":
            return True

        if self.rate is None:
            return True

        self.key = self.get_cache_key(request, view)
        if self.key is None:
            return True

        self.history = self.cache.get(self.key, [])
        self.now = self.timer()

        # Drop any requests from the history which have now passed the
        # throttle duration
        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()
        if len(self.history) >= self.num_requests:
            return self.throttle_failure()
        return self.throttle_success()

    def throttle_success(self):
        """
        Inserts the current request's timestamp along with the key
        into the cache.
        """
        self.history.insert(0, self.now)
        self.cache.set(self.key, self.history, self.duration)
        return True

    def throttle_failure(self):
        """
        Called when a request to the API has failed due to throttling.
        """
        return False

    # def wait(self):
    #     """
    #     Returns the recommended next request time in seconds.
    #     """
    #     if self.history:
    #         remaining_duration = self.duration - (self.now - self.history[-1])
    #     else:
    #         remaining_duration = self.duration
    #
    #     available_requests = self.num_requests - len(self.history) + 1
    #     if available_requests <= 0:
    #         return None
    #
    #     return remaining_duration / float(available_requests)
