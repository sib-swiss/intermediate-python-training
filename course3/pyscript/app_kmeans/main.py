import altair as alt
import panel as pn
import pandas as pd
import param

from sklearn.cluster import KMeans
from pyodide.http import open_url

pn.config.sizing_mode = 'stretch_width'

url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-28/penguins.csv'
penguins = pd.read_csv(open_url(url)).dropna()
cols = list(penguins.columns)[2:6]

x = pn.widgets.Select(name='x', options=cols, value='bill_depth_mm').servable(target='x-widget')
y = pn.widgets.Select(name='y', options=cols, value='bill_length_mm').servable(target='y-widget')
n_clusters = pn.widgets.IntSlider(name='n_clusters', start=1, end=5, value=3).servable(target='n-widget')

brush = alt.selection_interval(name='brush')  # selection of type "interval"

def get_clusters(n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, n_init=10)
    est = kmeans.fit(penguins[cols].values)
    df = penguins.copy()
    df['labels'] = est.labels_.astype('str')
    return df

def get_chart(x, y, df):
    centers = df.groupby('labels').mean(numeric_only=True)
    return (
        alt.Chart(df)
            .mark_point(size=100)
            .encode(
                x=alt.X(x, scale=alt.Scale(zero=False)),
                y=alt.Y(y, scale=alt.Scale(zero=False)),
                shape='labels',
                color='species'
            ).add_params(brush).properties(width=800) +
        alt.Chart(centers)
            .mark_point(size=250, shape='cross', color='black')
            .encode(x=x+':Q', y=y+':Q')
    )

intro = pn.pane.Markdown("""
This app provides an example of **building a simple dashboard using
Panel**.\n\nIt demonstrates how to take the output of **k-means
clustering on the Penguins dataset** using scikit-learn,
parameterizing the number of clusters and the variables to
plot.\n\nThe **`x` marks the center** of
the cluster.
""").servable(target='intro')

chart = pn.pane.Vega().servable(target='cluster-plot')
table = pn.widgets.Tabulator(pagination='remote', page_size=10).servable(target='table')

def update_table(event=None):
    table.value = get_clusters(n_clusters.value)

n_clusters.param.watch(update_table, 'value')

@pn.depends(x, y, n_clusters, watch=True)
def update_chart(*events):
    chart.object = get_chart(x.value, y.value, table.value)

@param.depends('brush', watch=True)
def update_filters(event=None):
    filters = []
    for k, v in (getattr(event, 'new') or {}).items():
        filters.append(dict(field=k, type='>=', value=v[0]))
        filters.append(dict(field=k, type='<=', value=v[1]))
    table.filters = filters


update_table()
update_chart()

