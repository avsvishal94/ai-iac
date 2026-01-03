def estimate(resources):
    cost = 0

    for r in resources:
        if "eks" in r["type"]:
            cost += 150
        if "alb" in r["type"]:
            cost += 20

    return {
        "monthly_cost_usd": cost,
        "confidence": "low"
    }
