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
            <div v-for="tweet in tweets" :key="tweet.id" class="tweets">
              <div class="container">
                <div class="row justify-content-md-center">
                  <div class="card" style="width: 18rem">
                    <div class="card-body">
                      <ul>
                        <li><strong>Tweet Title:</strong> {{ tweet.title }}</li>
                        <li>
                          <strong>Author:</strong> {{ tweet.author.username }}
                        </li>
                        <li>
                          <router-link
                            :to="{ name: 'Tweet', params: { id: tweet.id } }"
                            >View</router-link
                          >
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
              <br />
            </div>
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
      this.form.title = "";
      this.form.content = "";
    },
  },
};
</script>
