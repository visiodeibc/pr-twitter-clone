<template>
  <section>
    <div v-if="tweets.length">
      <div v-for="tweet in tweets" :key="tweet.id" class="tweets">
        <div class="card" style="width: 18rem">
          <div class="card-body">
            <ul>
              <li><strong>Tweet Title:</strong> {{ tweet.title }}</li>
              <li><strong>Content:</strong> {{ tweet.content }}</li>
              <li><strong>Author:</strong> {{ tweet.author.username }}</li>
              <li>
                <router-link :to="{ name: 'Tweet', params: { id: tweet.id } }"
                  >View</router-link
                >
              </li>
            </ul>
          </div>
        </div>
        <br />
      </div>
    </div>
    <div v-else>
      <p>This site is built with FastAPI and Vue.</p>
      <div v-if="isLoggedIn" id="logout">
        <p id="logout">
          Click <a href="/dashboard">here</a> to view all tweetss.
        </p>
      </div>
      <p v-else>
        <span><a href="/register">Register</a></span>
        <span> or </span>
        <span><a href="/login">Log In</a></span>
      </p>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Dashboard",
  data() {
    return {
      form: {
        title: "",
        content: "",
      },
    };
  },
  created: function () {
    return this.$store.dispatch("getTweets");
  },
  computed: {
    ...mapGetters({ tweets: "stateTweets" }),
  },
  methods: {
    ...mapActions(["createTweet"]),
    async submit() {
      await this.createTweet(this.form);
    },
  },
};
</script>
