class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        n = len(s)

        # window size starts from len(t)
        for w in range(len(t), n + 1):
            window_count = Counter()

            # build first window of size w
            for i in range(w):
                window_count[s[i]] += 1

            # check first window
            if self.is_valid(window_count, t_count):
                return s[0:w]

            # slide window
            for i in range(w, n):
                window_count[s[i]] += 1
                window_count[s[i - w]] -= 1

                if self.is_valid(window_count, t_count):
                    return s[i - w + 1 : i + 1]

        return ""

    def is_valid(self, window, target):
        for ch in target:
            if window[ch] < target[ch]:
                return False
        return True