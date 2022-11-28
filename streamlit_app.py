"""
# Welcome to Streamlit!
    st.altair_chart(
        pandasamlit_downloads(selected_data_streamlit), use_container_width=True
    )

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
    # OTHER DOWNLOADS

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
    st.header("Compare other package downloads")

In the meantime, below is an example of what you can do with just a few lines of code:
"""
    instructions = """
    Click and drag line chart to select and pan date interval\n
    Hover over bar chart to view downloads\n
    Click on a bar to highlight that package
    """
    select_packages = st.multiselect(
        "Select Python packages to compare",
        package_names,
        default=[
            "pandas",
            "keras",
        ],
        help=instructions,
    )

    select_packages_df = pd.DataFrame(select_packages).rename(columns={0: "project"})

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
    if not select_packages:
        st.stop()

    Point = namedtuple('Point', 'x y')
    data = []
    filtered_df = selected_data_all[
        selected_data_all["project"].isin(select_packages_df["project"])
    ]

    points_per_turn = total_points / num_turns
    st.altair_chart(plot_all_downloads(filtered_df), use_container_width=True)

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
st.title("Downloads")
st.write(
    "Metrics on how often Pandas is being downloaded from PyPI (Python's main "
    "package repository, i.e. where `pip install pandas` downloads the package from)."
)
main()
