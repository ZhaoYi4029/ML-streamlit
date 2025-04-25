import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import altair as alt

st.title('📊Clustering Algorithm Dashboard')


if st.checkbox("Show PCA scatter of clustered data", value=True):
    # Run PCA on the scaled feature matrix used for clustering
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)   

    # Build a small DataFrame for plotting
    pca_df = pd.DataFrame({
        "PC1": X_pca[:,0],
        "PC2": X_pca[:,1],
        "Cluster": labels.astype(str)     
    })

    #  Plot with Altair
    chart = (
        alt.Chart(pca_df)
           .mark_circle(size=60, opacity=0.7)
           .encode(
               x="PC1",
               y="PC2",
               color=alt.Color("Cluster", legend=alt.Legend(title="Cluster ID")),
               tooltip=["PC1","PC2","Cluster"]
           )
           .properties(
               width=600, height=400,
               title="PCA: first two components"
           )
           .interactive()
    )
    st.altair_chart(chart, use_container_width=True)

    # Optional: show explained variance
    explained = pca.explained_variance_ratio_
    st.write(f"Explained variance: PC1={explained[0]:.2%}, PC2={explained[1]:.2%}")
