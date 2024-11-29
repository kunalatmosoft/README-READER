import streamlit as st
import requests
import pandas as pd

# Set the page configuration
st.set_page_config(
    page_title="GitHub ID Improvement Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Description
st.title("🚀 GitHub ID Improvement Platform")
st.markdown("""
Welcome to the GitHub ID Improvement Platform! 🎉  
Enter your GitHub username, and we'll analyze your profile to provide personalized recommendations to level up your GitHub game.  
Get ready to unlock your full potential! 💪
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
        We're thrilled to have you here! 🥳 Let's analyze your GitHub profile and uncover opportunities to make it even more impressive. 🚀
        """)

        # Display Basic Profile Information
        st.image(user_data['avatar_url'], width=150)
        st.markdown(f"**Name:** {user_data.get('name', 'N/A')}")
        st.markdown(f"**Bio:** {user_data.get('bio', 'N/A')}")
        st.markdown(f"**Public Repos:** {user_data['public_repos']}")
        st.markdown(f"**Followers:** {user_data['followers']} 👥")
        st.markdown(f"**Following:** {user_data['following']} ✅")
        st.markdown(f"[🌐 View Profile]({user_data['html_url']})")

        # Recommendations Section
        st.subheader("✨ Personalized Recommendations for Your GitHub Profile")

        recommendations = []

        # Check for bio
        if not user_data.get('bio'):
            recommendations.append("📝 Add a bio to your profile to make it more engaging and informative.")

        # Check for profile picture
        if user_data['avatar_url'].endswith("no_avatar.png"):
            recommendations.append("📸 Upload a profile picture to make your account more personal.")

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

        # General Recommendations
        recommendations.append("🌟 Pin your best repositories to highlight your skills.")
        recommendations.append("📄 Add a README.md file to your repositories to describe your projects.")
        recommendations.append("🎨 Use topics and tags to improve the discoverability of your repositories.")
        recommendations.append("💡 Contribute to open-source projects to gain visibility and experience.")
        recommendations.append("⚡ Leverage GitHub Actions to showcase automation and DevOps skills.")
        recommendations.append("📈 Showcase projects with data visualizations or innovative tools.")
        recommendations.append("✅ Write clear and descriptive commit messages to make your contributions professional.")
        recommendations.append("🛠️ Participate in Hacktoberfest or other open-source events to expand your network.")

        # Display Recommendations
        st.markdown("Here's what you can do to improve your profile:")
        for rec in recommendations:
            st.markdown(f"- {rec}")

        # Repository Analysis
        st.subheader("🔍 Repository Analysis")
        repo_df = pd.DataFrame(repos_data, columns=['name', 'stargazers_count', 'forks_count', 'html_url'])
        if not repo_df.empty:
            repo_df = repo_df.rename(columns={
                'name': 'Repository Name',
                'stargazers_count': 'Stars',
                'forks_count': 'Forks',
                'html_url': 'URL'
            })
            repo_df = repo_df.sort_values(by='Stars', ascending=False)
            st.markdown("📊 Here's a summary of your repositories:")
            st.dataframe(repo_df[['Repository Name', 'Stars', 'Forks']])
    else:
        st.error("❌ Unable to fetch data. Please check the username and try again.")

# Footer
st.markdown("""
---
Built with ❤️ using [Streamlit](https://streamlit.io/) and the [GitHub API](https://docs.github.com/en/rest).
""")
