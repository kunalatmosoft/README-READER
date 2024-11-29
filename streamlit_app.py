import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration
st.set_page_config(
    page_title="🚀 Advanced GitHub Improvement Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Description
st.title("🌟 Advanced GitHub ID Improvement Platform")
st.markdown("""
Welcome to the next level of GitHub analytics! 🎉  
This platform provides advanced visualizations, profile analysis, and actionable recommendations to enhance your GitHub presence.  
""")

# Input: GitHub Username
github_username = st.text_input("🔑 Enter Your GitHub Username")

if github_username:
    # Fetch GitHub User Data
    user_url = f"https://api.github.com/users/{github_username}"
    repos_url = f"https://api.github.com/users/{github_username}/repos"

    user_response = requests.get(user_url)
    repos_response = requests.get(repos_url)

    if user_response.status_code == 200 and repos_response.status_code == 200:
        user_data = user_response.json()
        repos_data = repos_response.json()

        # Friendly Introduction
        st.subheader(f"👋 Hi, {user_data.get('name', user_data['login'])}!")
        st.markdown("Here's a personalized analysis of your GitHub profile. Let’s get started! 🚀")

        # Display Basic Profile Information
        st.image(user_data['avatar_url'], width=150)
        st.markdown(f"**Name:** {user_data.get('name', 'N/A')}")
        st.markdown(f"**Bio:** {user_data.get('bio', 'N/A')}")
        st.markdown(f"**Public Repos:** {user_data['public_repos']}")
        st.markdown(f"**Followers:** {user_data['followers']} 👥")
        st.markdown(f"**Following:** {user_data['following']} ✅")
        st.markdown(f"[🌐 View Profile]({user_data['html_url']})")

        # Profile Scoring
        st.subheader("📊 Profile Score")
        score = 50  # Base score
        if user_data.get('bio'):
            score += 10
        if user_data['public_repos'] > 5:
            score += 15
        if user_data['followers'] > 20:
            score += 10
        if len(repos_data) > 0:
            score += 15
        st.metric("Your GitHub Profile Score", f"{score}/100")

        # Repository Insights
        st.subheader("🔍 Repository Insights")
        if repos_data:
            repo_df = pd.DataFrame(repos_data)
            repo_df = repo_df[['name', 'stargazers_count', 'forks_count', 'pushed_at', 'html_url']]
            repo_df['pushed_at'] = pd.to_datetime(repo_df['pushed_at'])

            # Graph Options for Stars and Forks
            graph_option = st.selectbox(
                "Select Graph Type for Repository Insights:",
                ["Bar Chart", "Pie Chart"]
            )
            if graph_option == "Bar Chart":
                fig, ax = plt.subplots()
                sns.barplot(
                    data=repo_df.sort_values('stargazers_count', ascending=False),
                    x='stargazers_count',
                    y='name',
                    palette='viridis',
                    ax=ax
                )
                ax.set_title("Repositories by Stars")
                ax.set_xlabel("Stars")
                ax.set_ylabel("Repository Name")
                st.pyplot(fig)
            elif graph_option == "Pie Chart":
                pie_data = repo_df[['name', 'stargazers_count']].set_index('name')
                pie_data = pie_data[pie_data['stargazers_count'] > 0]
                fig, ax = plt.subplots()
                ax.pie(
                    pie_data['stargazers_count'],
                    labels=pie_data.index,
                    autopct='%1.1f%%',
                    startangle=90,
                    colors=sns.color_palette('pastel')
                )
                ax.set_title("Stars Distribution Across Repositories")
                st.pyplot(fig)

        # Language Distribution
        st.subheader("🖍️ Language Distribution")
        language_data = {}
        for repo in repos_data:
            language_url = repo['languages_url']
            language_response = requests.get(language_url).json()
            for lang, size in language_response.items():
                language_data[lang] = language_data.get(lang, 0) + size

        if language_data:
            lang_df = pd.DataFrame(list(language_data.items()), columns=["Language", "Size"])
            graph_option_lang = st.selectbox(
                "Select Graph Type for Language Distribution:",
                ["Pie Chart", "Bar Chart"]
            )
            if graph_option_lang == "Pie Chart":
                fig, ax = plt.subplots()
                ax.pie(
                    lang_df['Size'],
                    labels=lang_df['Language'],
                    autopct='%1.1f%%',
                    startangle=90,
                    colors=sns.color_palette('bright')
                )
                ax.set_title("Language Usage Distribution")
                st.pyplot(fig)
            elif graph_option_lang == "Bar Chart":
                fig, ax = plt.subplots()
                sns.barplot(
                    data=lang_df,
                    x='Size',
                    y='Language',
                    palette='coolwarm',
                    ax=ax
                )
                ax.set_title("Language Usage by Size")
                st.pyplot(fig)

        # Activity Analysis
        st.subheader("📅 Repository Activity Analysis")
        repo_df = repo_df.sort_values(by='pushed_at', ascending=True)
        st.line_chart(repo_df.set_index('pushed_at')['stargazers_count'])

        # Recommendations Section
        st.subheader("✨ Personalized Recommendations")
        recommendations = []

        # Add more dynamic recommendations
        if not user_data.get('bio'):
            recommendations.append("📝 Add a bio to make your profile more engaging.")
        if user_data['followers'] < 10:
            recommendations.append("🤝 Increase your followers by contributing to discussions.")
        if len(repos_data) < 5:
            recommendations.append("📂 Create more repositories to showcase your projects.")
        recommendations.append("🌟 Pin top repositories to highlight your best work.")
        recommendations.append("💡 Add a README.md file to each repository.")
        recommendations.append("📄 Write clear documentation for your projects.")
        recommendations.append("⚡ Use GitHub Actions to automate your workflows.")

        for rec in recommendations:
            st.markdown(f"- {rec}")

    else:
        st.error("❌ Unable to fetch data. Please check the username and try again.")

# Footer
st.markdown("""
---
Built with ❤️ using [Streamlit](https://streamlit.io/) and the [GitHub API](https://docs.github.com/en/rest).
""")
