from flask import Flask, render_template, request

app = Flask(__name__)

# AI-generated scoring function
def calculate_score(touchdowns, field_goals, safeties, extra_points):
    """Returns a team's total score based on NFL rules."""
    return (touchdowns * 6) + (field_goals * 3) + (safeties * 2) + extra_points


@app.route("/", methods=["GET", "POST"])
def index():
    total = None

    if request.method == "POST":
        tds = int(request.form.get("touchdowns", 0))
        fgs = int(request.form.get("field_goals", 0))
        safeties = int(request.form.get("safeties", 0))
        xps = int(request.form.get("extra_points", 0))

        total = calculate_score(tds, fgs, safeties, xps)

    return render_template("index.html", total=total)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    result = None

    if request.method == "POST":
        team_a = request.form.get("team_a")
        team_b = request.form.get("team_b")
        avg_a = float(request.form.get("avg_a", 0))
        avg_b = float(request.form.get("avg_b", 0))

        if avg_a > avg_b:
            result = f"{team_a} is likely to win based on scoring averages."
        elif avg_b > avg_a:
            result = f"{team_b} is likely to win based on scoring averages."
        else:
            result = "It looks like an even matchup!"

    return render_template("predictor.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
