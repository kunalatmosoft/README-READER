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
st.title("GitHub ID Improvement Platform")
st.markdown("""
Enter your GitHub username, and this platform will provide actionable recommendations 
to improve your profile, such as enhancing repositories, contributing to open-source projects, 
and improving your overall profile visibility.
""")

# Input: GitHub Username
github_username = st.text_input("Enter Your GitHub Username")

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
        st.subheader(f"Hello, {user_data.get('name', user_data['login'])}! 👋")
        st.markdown("It's great to have you here. Let's explore ways to enhance your GitHub presence!")

        # Display Basic Profile Information
        st.image(user_data['avatar_url'], width=150)
        st.markdown(f"**Name:** {user_data.get('name', 'N/A')}")
        st.markdown(f"**Bio:** {user_data.get('bio', 'N/A')}")
        st.markdown(f"**Public Repos:** {user_data['public_repos']}")
        st.markdown(f"**Followers:** {user_data['followers']}")
        st.markdown(f"**Following:** {user_data['following']}")
        st.markdown(f"[View Profile]({user_data['html_url']})")

        # Recommendations Section
        st.subheader("Personalized Recommendations to Improve Your GitHub Profile")

        recommendations = []

        # Check for bio
        if not user_data.get('bio'):
            recommendations.append("Add a bio to your profile to make it more engaging.")

        # Check for profile picture
        if user_data['avatar_url'].endswith("no_avatar.png"):
            recommendations.append("Upload a profile picture to make your account more personal.")

        # Check for repository activity
        if len(repos_data) == 0:
            recommendations.append("Start creating repositories to showcase your projects.")
        else:
            active_repos = [repo for repo in repos_data if repo['pushed_at']]
            if len(active_repos) == 0:
                recommendations.append("Update your repositories with recent activity.")

        # Check for followers
        if user_data['followers'] < 10:
            recommendations.append("Engage with the community to gain more followers.")

        # Provide generic recommendations
        recommendations.append("Contribute to open-source projects to gain visibility.")
        recommendations.append("Add a README.md file to your repositories to describe your projects.")
        recommendations.append("Pin your best repositories to your profile to highlight your skills.")
        recommendations.append("Participate in GitHub discussions and forums to enhance community engagement.")
        recommendations.append("Add topics to your repositories to improve discoverability.")
        recommendations.append("Use GitHub Actions to automate workflows and showcase DevOps skills.")
        recommendations.append("Create repositories for personal projects to demonstrate innovation.")
        recommendations.append("Write detailed commit messages to make your contributions more professional.")
        recommendations.append("Collaborate on repositories by participating in pull requests to show teamwork skills.")
        recommendations.append("Showcase data visualizations, APIs, or other tools in your projects to demonstrate expertise.")
        recommendations.append("Participate in Hacktoberfest or similar events to grow your network.")

        st.markdown("Here are some tips just for you:")
        for rec in recommendations:
            st.markdown(f"- {rec}")

        # Repository Analysis
        st.subheader("Repository Analysis")
        repo_df = pd.DataFrame(repos_data, columns=['name', 'stargazers_count', 'forks_count', 'html_url'])
        if not repo_df.empty:
            repo_df = repo_df.rename(columns={
                'name': 'Repository Name',
                'stargazers_count': 'Stars',
                'forks_count': 'Forks',
                'html_url': 'URL'
            })
            repo_df = repo_df.sort_values(by='Stars', ascending=False)
            st.dataframe(repo_df[['Repository Name', 'Stars', 'Forks']])
    else:
        st.error("Unable to fetch data. Please check the username and try again.")

# Footer
st.markdown("""
---
Built with [Streamlit](https://streamlit.io/) and the [GitHub API](https://docs.github.com/en/rest).
""")
