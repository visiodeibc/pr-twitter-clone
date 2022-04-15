<template>
  <div class="container">
    <div class="row justify-content-md-center">
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
    </div>
  </div>
</template>

<script>
export default {
  name: "Tweet",
  props: ["tweet"],
};
</script>
