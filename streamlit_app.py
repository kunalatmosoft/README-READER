import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

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
We'll evaluate your GitHub profile, provide actionable recommendations, and offer advanced visualizations 
to help you stand out as a developer. Let's get started! 💻
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
        st.markdown("""
        Here's a personalized analysis of your GitHub profile.  
        Let's explore opportunities to shine brighter in the GitHub community! 🚀
        """)

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

        # Recommendations Section
        st.subheader("✨ Personalized Recommendations")
        recommendations = []

        # Check for bio
        if not user_data.get('bio'):
            recommendations.append("📝 Add a bio to your profile to make it more engaging and informative.")
        
        # Check for repository activity
        if len(repos_data) == 0:
            recommendations.append("📂 Start creating repositories to showcase your projects and skills.")
        else:
            active_repos = [repo for repo in repos_data if repo['pushed_at']]
            if len(active_repos) == 0:
                recommendations.append("⚙️ Update your repositories with recent activity to show you’re active.")

        # Check for followers
        if user_data['followers'] < 10:
            recommendations.append("🤝 Engage with the community to gain more followers. Try following people and contributing to discussions!")

        # Additional recommendations
        recommendations.append("🌟 Pin your best repositories to highlight your skills.")
        recommendations.append("📄 Add a README.md file to your repositories to describe your projects.")
        recommendations.append("🎨 Use topics and tags to improve the discoverability of your repositories.")
        recommendations.append("💡 Contribute to open-source projects to gain visibility and experience.")
        recommendations.append("⚡ Leverage GitHub Actions to showcase automation and DevOps skills.")

        for rec in recommendations:
            st.markdown(f"- {rec}")

        # Repository Insights
        st.subheader("🔍 Repository Insights")
        if repos_data:
            repo_df = pd.DataFrame(repos_data)
            most_starred = repo_df.loc[repo_df['stargazers_count'].idxmax()]
            st.markdown(f"🌟 Your most popular repository is **{most_starred['name']}** with {most_starred['stargazers_count']} stars!")
            st.markdown(f"[🔗 View Repository]({most_starred['html_url']})")

        # Language Distribution Chart
        st.subheader("🖍️ Language Distribution")
        language_data = {}
        for repo in repos_data:
            language_url = repo['languages_url']
            language_response = requests.get(language_url).json()
            for lang, size in language_response.items():
                if lang in language_data:
                    language_data[lang] += size
                else:
                    language_data[lang] = size

        if language_data:
            lang_df = pd.DataFrame(list(language_data.items()), columns=["Language", "Size"])
            fig, ax = plt.subplots()
            ax.pie(lang_df["Size"], labels=lang_df["Language"], autopct="%1.1f%%")
            ax.set_title("Programming Language Distribution")
            st.pyplot(fig)

        # Community Engagement Metrics
        st.subheader("📈 Community Engagement")
        st.markdown(f"👥 **Followers**: {user_data['followers']} (Try reaching 50!)")
        st.markdown(f"🤝 **Following**: {user_data['following']} (Engage with more people!)")
        st.markdown(f"📂 **Repositories**: {len(repos_data)} (Aim for 10+!)")

        # Repository Activity Trends
        st.subheader("📅 Repository Activity")
        activity_df = pd.DataFrame(repos_data, columns=["name", "pushed_at"])
        activity_df["pushed_at"] = pd.to_datetime(activity_df["pushed_at"])
        activity_df = activity_df.sort_values("pushed_at", ascending=True)
        st.line_chart(activity_df.set_index("pushed_at")["name"])

    else:
        st.error("❌ Unable to fetch data. Please check the username and try again.")

# Footer
st.markdown("""
---
Built with ❤️ using [Streamlit](https://streamlit.io/) and the [GitHub API](https://docs.github.com/en/rest).
""")
