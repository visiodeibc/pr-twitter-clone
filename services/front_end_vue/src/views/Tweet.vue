<template>
  <div v-if="tweet">
    <p><strong>Title:</strong> {{ tweet.title }}</p>
    <p><strong>Content:</strong> {{ tweet.content }}</p>
    <p><strong>Author:</strong> {{ tweet.author.username }}</p>

    <div v-if="user.id === tweet.author.id">
      <p><router-link :to="{name: 'EditTweet', params:{id: tweet.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeTweet()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Tweet',
  props: ['id'],
  async created() {
    try {
      await this.viewTweet(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ tweet: 'stateTweet', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewTweet', 'deleteTweet']),
    async removeTweet() {
      try {
        await this.deleteTweet(this.id);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error(error);
      }
    }
  },
};
</script>