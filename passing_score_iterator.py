class PassingScoreIterator:
    """Iterator to iterate over scores equal to or above a passing threshold."""

    def __init__(self, scores, passing_threshold):
        """Initialize the PassingScoreIterator.

        Args:
            scores (list): List of student scores.
            passing_threshold (int): The minimum passing score.
        """
        self.scores = scores
        self.passing_threshold = passing_threshold
        self.index = 0

    def __iter__(self):
        """Return the iterator object."""
        return self

    def __next__(self):
        """Return the next passing score."""
        while self.index < len(self.scores):
            score = self.scores[self.index]
            self.index += 1
            if score >= self.passing_threshold:
                return score
        raise StopIteration

def passing_scores(scores, passing_threshold):
    """Generator function to yield passing scores.

    Args:
        scores (list): List of student scores.
        passing_threshold (int): The minimum passing score.

    Yields:
        int: Passing score.
    """
    for score in scores:
        if score >= passing_threshold:
            yield score

# Example usage:
scores = [65, 70, 80, 90, 55, 40, 75]
passing_threshold = 60
passing_scores_iter = PassingScoreIterator(scores, passing_threshold)
pass_iter = iter(PassingScoreIterator(scores, passing_threshold))
print(next(pass_iter))
print(next(pass_iter))
print(next(pass_iter))
print(next(pass_iter))
print(next(pass_iter))
print('***')
for score in passing_scores_iter:
    print(score)
print('***')
for score in passing_scores(scores, passing_threshold):
    print(score)
