<template>
  <section>
    <h1>Edit tweet</h1>
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
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "EditTweet",
  props: ["id"],
  data() {
    return {
      form: {
        title: "",
        content: "",
        public: "",
      },
    };
  },
  created: function () {
    this.GetTweet();
  },
  computed: {
    ...mapGetters({ tweet: "stateTweet" }),
  },
  methods: {
    ...mapActions(["updateTweet", "viewTweet"]),
    async submit() {
      try {
        console.log(this.form)
        let tweet = {
          id: this.id,
          form: this.form,
        };
        await this.updateTweet(tweet);
        this.$router.push({ name: "Tweet", params: { id: this.tweet.id } });
      } catch (error) {
        console.log(error);
      }
    },
    async GetTweet() {
      try {
        await this.viewTweet(this.id);
        this.form.title = this.tweet.title;
        this.form.content = this.tweet.content;
        this.form.public = this.tweet.public;
      } catch (error) {
        console.error(error);
        this.$router.push("/dashboard");
      }
    },
  },
};
</script>
