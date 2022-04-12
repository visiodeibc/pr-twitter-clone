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
    <!-- <div v-else>
      <h2>This site is built with FastAPI and Vue.</h2>
      <div v-if="isLoggedIn" id="logout">
        <h3>

          You don't have any Tweet! Go tweet!!
        </h3>
      </div>
      <p v-else>
        <span><a href="/register">Register</a></span>
        <span> or </span>
        <span><a href="/login">Log In</a></span>
      </p>
    </div> -->
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Dashboard",
  created: function () {
    return this.$store.dispatch("getTweets");
  },
  computed: {
    ...mapGetters({ tweets: "stateTweets" }),
    // isLoggedIn: function () {
    //   return this.$store.getters.isAuthenticated;
    // },
  },
};
</script>
