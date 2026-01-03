def recommend(cost):
    recs = []

    if cost > 300:
        recs.append("Use Spot instances for non-prod clusters")

    return recs
