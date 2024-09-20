def test_review_string(review):
    assert str(review) == f"{review.song} | {review.stars}"
