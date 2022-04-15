<template>
  <section>
    <h1>Your Profile</h1>
    <hr />
    <br />
    <div>
      <p>
        <strong>Full Name:</strong> <span>{{ user.full_name }}</span>
      </p>
      <p>
        <strong>Username:</strong> <span>{{ user.username }}</span>
      </p>

      <div class="container">
        <div class="row justify-content-md-center">
          <p>
            <router-link
              :to="{ name: 'EditUser', params: { id: user.id } }"
              class="btn btn-primary btn-lg btn-block m-2"
            >
              Edit Account</router-link
            >

            <button
              @click="deleteAccount()"
              class="btn btn-danger btn-lg btn-block m-2"
            >
              Delete Account
            </button>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Profile",
  created: function () {
    return this.$store.dispatch("viewMe");
  },
  computed: {
    ...mapGetters({ user: "stateUser" }),
  },
  methods: {
    ...mapActions(["deleteUser"]),
    async deleteAccount() {
      try {
        await this.deleteUser(this.user.id);
        await this.$store.dispatch("logOut");
        this.$router.push("/");
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
