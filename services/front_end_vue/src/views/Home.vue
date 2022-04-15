<template>
  <section>
    <div class="text-center">
      <h1>All Tweets</h1>
      <hr />
    </div>
    <br />
    <div v-if="tweets.length">
      <Tweet
        v-for="tweet in tweets"
        v-bind:key="tweet.id"
        v-bind:tweet="tweet"
      ></Tweet>
      <br />
    </div>
    <div v-else>
      <h2>This site is built with FastAPI and Vue.</h2>
      <h3>You don't have any Tweet! Go tweet!!</h3>
    </div>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
import Tweet from "../components/Tweet.vue";

export default {
  name: "Dashboard",
  components: {
    Tweet,
  },
  created: function () {
    return this.$store.dispatch("getAllPublicTweets");
  },
  computed: {
    ...mapGetters({ tweets: "statePublicTweets" }),
    // isLoggedIn: function () {
    //   return this.$store.getters.isAuthenticated;
    // },
  },
};
</script>
