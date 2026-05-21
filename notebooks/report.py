import marimo

__generated_with = "0.10.0"
app = marimo.App()

@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import altair as alt
    return mo, pd, alt

@app.cell
def __(mo, pd, alt):
    df = pd.read_csv("data/features/events.csv")

    chart = alt.Chart(df).mark_bar().encode(
        alt.X("duration_minutes:Q", bin=alt.Bin(maxbins=30), title="Duration (minutes)"),
        alt.Y("count()", title="Count"),
    ).properties(
        title="Distribution of Event Durations"
    )

    mo.ui.altair_chart(chart)

if __name__ == "__main__":
    app.run()
