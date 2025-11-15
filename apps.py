import streamlit as st
import preprocessors, helper
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# HOME PAGE
# =============================
def home():
    st.title("Welcome to WhatsApp Chat Analyzer (24-Hour)")
    st.markdown("""
        This version is configured for **24-hour timestamp WhatsApp chats**.
        Upload your `.txt` file and start analyzing messages, media, links,
        sentiment, emojis, weekly/monthly activity, and more.
    """)

# =============================
# ANALYSIS PAGE
# =============================
def analyze():
    st.title("WhatsApp Chat Analysis (24-Hour Format)")
    st.sidebar.title("WhatsApp Chat Analyzer")

    uploaded_file = st.sidebar.file_uploader("Choose a WhatsApp Chat File (.txt)")

    if uploaded_file is not None:
        data = uploaded_file.getvalue().decode("utf-8")

        # use 24-hour preprocessors file
        df = preprocessors.preprocess(data)

        # fetch users
        user_list = df['user'].unique().tolist()
        if 'group_notification' in user_list:
            user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0, "Overall")

        selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

        if st.sidebar.button("Show Analysis"):

            # =============================
            # Top Statistics
            # =============================
            num_messages, words, num_media, num_links = helper.fetch_stats(selected_user, df)

            st.title("Top Statistics")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.header("Total Messages")
                st.title(num_messages)
            with col2:
                st.header("Total Words")
                st.title(words)
            with col3:
                st.header("Media Shared")
                st.title(num_media)
            with col4:
                st.header("Links Shared")
                st.title(num_links)

            # =============================
            # Sentiment Analysis
            # =============================
            st.title("Sentiment Analysis")
            sentiment_df = helper.sentiment_analysis(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(sentiment_df['sentiment_label'], sentiment_df['message'])
            st.pyplot(fig)

            # =============================
            # Emoji Analysis
            # =============================
            st.title("Emoji Analysis")
            emoji_df = helper.emoji_helper(selected_user, df)
            col1, col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)
            with col2:
                fig, ax = plt.subplots()
                ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
                st.pyplot(fig)

            # =============================
            # Monthly Timeline
            # =============================
            st.title("Monthly Timeline")
            timeline = helper.monthly_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'])
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            # =============================
            # Daily Timeline
            # =============================
            st.title("Daily Timeline")
            daily = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily['only_date'], daily['message'])
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            # =============================
            # Activity Maps
            # =============================
            st.title('Activity Map')
            c1, c2 = st.columns(2)

            with c1:
                st.header("Most Busy Day")
                busy_day = helper.week_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_day.index, busy_day.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with c2:
                st.header("Most Busy Month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_month.index, busy_month.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            # Heatmap
            st.title("Weekly Activity Heatmap")
            heatmap = helper.activity_heatmap(selected_user, df)
            fig, ax = plt.subplots()
            sns.heatmap(heatmap, ax=ax)
            st.pyplot(fig)

            # =============================
            # Most Busy Users
            # =============================
            if selected_user == "Overall":
                st.title("Most Busy Users")
                x, new_df = helper.most_busy_users(df)

                c1, c2 = st.columns(2)
                with c1:
                    fig, ax = plt.subplots()
                    ax.bar(x.index, x.values)
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)
                with c2:
                    st.dataframe(new_df)

            # =============================
            # Wordcloud
            # =============================
            st.title("Wordcloud")
            wc = helper.create_wordcloud(selected_user, df)
            fig, ax = plt.subplots()
            ax.imshow(wc)
            st.pyplot(fig)

            # =============================
            # Most Common Words
            # =============================
            st.title("Most Common Words")
            mc = helper.most_common_words(selected_user, df)
            fig, ax = plt.subplots()
            ax.barh(mc[0], mc[1])
            plt.xticks(rotation='vertical')
            st.pyplot(fig)


# =============================
# ABOUT
# =============================
def about_us():
    st.title("About Us - 24 Hour Version")
    st.write("Built by Gaurav Singh. Enhanced to support both YY and YYYY formats.")


# =============================
# SIDEBAR NAVIGATION
# =============================
st.sidebar.title("WhatsApp Chat Analyzer")
page = st.sidebar.radio("Go to", ["Home", "Analyze", "About Us"])

if page == "Home":
    home()
elif page == "Analyze":
    analyze()
else:
    about_us()
