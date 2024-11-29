import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit setup
st.set_page_config(page_title="Advanced GitHub Analytics", layout="wide", initial_sidebar_state="expanded")

# Title and description
st.title("🌟 GitHub ID Improvement Platform 🌟")
st.markdown("""
Welcome to your personalized GitHub guide! 👋 Enter your GitHub username below, and I'll provide 
friendly suggestions and deep insights to boost your GitHub game. 🚀
""")

# Input: GitHub Username
github_username = st.text_input("🔑 Enter Your GitHub Username")

if github_username:
    # Fetch GitHub user and repository data
    user_url = f"https://api.github.com/users/{github_username}"
    repos_url = f"https://api.github.com/users/{github_username}/repos"
    
    user_response = requests.get(user_url)
    repos_response = requests.get(repos_url)

    if user_response.status_code == 200 and repos_response.status_code == 200:
        user_data = user_response.json()
        repos_data = repos_response.json()

        # Friendly introduction
        st.subheader(f"Hello, {user_data.get('name', user_data['login'])}! 👋")
        st.markdown("I'm thrilled to assist you in making your GitHub profile shine. ✨ Let's start!")

        # Display profile details
        st.image(user_data['avatar_url'], width=150)
        st.markdown(f"**Name:** {user_data.get('name', 'N/A')}")
        st.markdown(f"**Bio:** {user_data.get('bio', 'N/A')}")
        st.markdown(f"**Public Repos:** {user_data['public_repos']}")
        st.markdown(f"**Followers:** {user_data['followers']}")
        st.markdown(f"**Following:** {user_data['following']}")
        st.markdown(f"[👉 View Profile Here]({user_data['html_url']})")

        # Recommendations
        st.subheader("💡 Recommendations to Improve Your GitHub Profile")
        recommendations = [
            "Add a bio to make your profile more engaging. ✍️",
            "Upload a profile picture to personalize your account. 🖼️",
            "Create repositories to showcase your projects. 📂",
            "Add a README.md file to each repository to explain its purpose. 📜",
            "Pin your best repositories on your profile to highlight your skills. 📌",
            "Contribute to open-source projects for visibility and collaboration. 🤝",
            "Write detailed commit messages to showcase professionalism. 📝",
            "Participate in Hacktoberfest or similar events to expand your network. 🌎",
            "Collaborate on pull requests to demonstrate teamwork. 👥",
            "Use GitHub Actions to automate workflows and showcase DevOps expertise. 🔄",
            "Engage with the community through GitHub discussions. 💬",
            "Add topics to your repositories to improve discoverability. 🔍",
            "Showcase APIs, data visualizations, or tools in your projects. 📊"
        ]

        # Advanced recommendations
        recommendations.extend([
            "Use GitHub Pages to host personal websites or project documentation. 🌐",
            "Regularly update repositories to reflect ongoing activity. 🔄",
            "Star repositories you find interesting to show involvement. ⭐",
            "Contribute to trending repositories to gain exposure. 🚀",
            "Leverage GitHub Sponsors to fund your open-source contributions. 💰",
            "Focus on securing your repositories by enabling branch protections. 🔒",
            "Organize repositories with clear folder structures and documentation. 🗂️",
            "Create interactive documentation using tools like MkDocs. 📚",
            "Add badges to your repository READMEs for better visual appeal. 🏷️",
            "Showcase skills with repositories in trending technologies (e.g., AI, blockchain). 🤖"
        ])

        st.markdown("Here are my personalized tips for you:")
        for rec in recommendations:
            st.markdown(f"- {rec}")

        # Language Distribution Section
        st.subheader("🖍️ Language Distribution")
        language_data = {}
        for repo in repos_data:
            language_url = repo['languages_url']
            language_response = requests.get(language_url).json()
            
            for lang, size in language_response.items():
                size = int(size)  # Ensure size is an integer
                language_data[lang] = language_data.get(lang, 0) + size

        if language_data:
            lang_df = pd.DataFrame(list(language_data.items()), columns=["Language", "Size"])

            # Graph for language distribution
            graph_option_lang = st.selectbox(
                "Select Graph Type for Language Distribution:",
                ["Pie Chart", "Bar Chart"]
            )

            if graph_option_lang == "Pie Chart":
                fig, ax = plt.subplots(figsize=(6, 6))
                ax.pie(
                    lang_df['Size'],
                    labels=lang_df['Language'],
                    autopct='%1.1f%%',
                    startangle=90,
                    colors=sns.color_palette('pastel')
                )
                ax.set_title("Language Usage Distribution", fontsize=14)
                st.pyplot(fig)

            elif graph_option_lang == "Bar Chart":
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.barplot(
                    data=lang_df.sort_values(by='Size', ascending=False),
                    x='Size',
                    y='Language',
                    palette='coolwarm',
                    ax=ax
                )
                ax.set_title("Language Usage by Size", fontsize=14)
                ax.set_xlabel("Code Size (bytes)", fontsize=12)
                ax.set_ylabel("Language", fontsize=12)
                st.pyplot(fig)

        # Repository Insights Section
        st.subheader("🔍 Repository Insights")
        repo_df = pd.DataFrame(repos_data, columns=['name', 'stargazers_count', 'forks_count', 'html_url'])
        repo_df.rename(columns={'name': 'Repository Name', 'stargazers_count': 'Stars', 'forks_count': 'Forks'}, inplace=True)

        # Graph for repository insights
        graph_option_repo = st.selectbox(
            "Select Graph Type for Repository Insights:",
            ["Bar Chart", "Pie Chart"]
        )

        if graph_option_repo == "Bar Chart":
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.barplot(
                data=repo_df.sort_values(by='Stars', ascending=False),
                x='Stars',
                y='Repository Name',
                palette='viridis',
                ax=ax
            )
            ax.set_title("Repositories by Stars", fontsize=14)
            ax.set_xlabel("Stars", fontsize=12)
            ax.set_ylabel("Repository Name", fontsize=12)
            st.pyplot(fig)

        elif graph_option_repo == "Pie Chart":
            pie_data = repo_df[repo_df['Stars'] > 0]
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.pie(
                pie_data['Stars'],
                labels=pie_data['Repository Name'],
                autopct='%1.1f%%',
                startangle=90,
                colors=sns.color_palette('pastel')
            )
            ax.set_title("Stars Distribution Across Repositories", fontsize=14)
            st.pyplot(fig)

    else:
        st.error("❌ Unable to fetch data. Please check the username and try again.")

# Footer
st.markdown("""
---
Built with ❤️ using [Streamlit](https://streamlit.io/) and the [GitHub API](https://docs.github.com/en/rest).
""")
