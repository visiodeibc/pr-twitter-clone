<template>
  <div>
    <div class="container">
      <div class="justify-content-md-center">
        <section>
          <h1>Add new Tweet</h1>
          <hr />
          <br />

          <form @submit.prevent="submit">
            <div class="mb-3">
              <label for="title" class="form-label">Title:</label>
              <input
                type="text"
                name="title"
                v-model="form.title"
                class="form-control"
              />
            </div>
            <div class="mb-3">
              <label for="content" class="form-label">Content:</label>
              <textarea
                name="content"
                v-model="form.content"
                class="form-control"
              ></textarea>
            </div>
            <div class="mb-3">
              <label for="public" class="form-label" style="padding-right: 10px"
                >Public:
              </label>
              <input
                type="checkbox"
                v-model="form.public"
                true-value=true
                false-value=false
              />
            </div>

            <div class="text-center">
              <button type="submit" class="btn btn-primary">Submit</button>
            </div>
          </form>
        </section>

        <br /><br />

        <section>
          <h1>Tweets</h1>
          <hr />
          <br />

          <div v-if="tweets.length">
            <Tweet
              v-for="tweet in tweets"
              v-bind:key="tweet.id"
              v-bind:tweet="tweet"
            ></Tweet>
          </div>

          <div v-else>
            <p>Nothing to see. Check back later.</p>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Tweet from "../components/Tweet.vue";

export default {
  name: "Dashboard",

  components: {
    Tweet,
  },

  data() {
    return {
      form: {
        title: "",
        content: "",
        public: true,
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
      // console.log(this.form.public);
      // console.log("checkbox".length);
      await this.createTweet(this.form);
      this.form.title = "";
      this.form.content = "";
      this.form.public = "";
    },
  },
};
</script>
