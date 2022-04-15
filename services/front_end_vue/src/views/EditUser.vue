<template>
  <section>
    <h1>Edit User Info</h1>
    <form @submit.prevent="submit">
      <div class="mb-3 w-50 mx-auto">
        <label for="username" class="form-label">Username:</label>
        <input
          type="text"
          name="username"
          v-model="form.username"
          class="form-control"
        />
      </div>
      <div class="mb-3 w-50 mx-auto">
        <label for="full_name" class="form-label">Full Name:</label>
        <input
          type="text"
          name="full_name"
          v-model="form.full_name"
          class="form-control"
        />
      </div>
      <div class="col text-center">
        <button type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "EditUser",
  props: ["id"],
  data() {
    return {
      form: {
        username: "",
        full_name: "",
      },
    };
  },
  created: function () {
    this.GetUser();
  },
  computed: {
    ...mapGetters({ user: "stateUser" }),
  },
  methods: {
    ...mapActions(["updateMe", "viewMe"]),
    async submit() {
      try {
        console.log(this.id),
        console.log(this.form)
        let user = {
          id: this.id,
          form: this.form,
        };
        await this.updateMe(user);
        //  this.$router.push({ name: "Tweet", params: { id: this.tweet.id } });
        //나중에 팝업으로 보여주거나 다른데로 리디랙팅
        // await this.register(this.user);
        // this.$router.push("/dashboard");
      } catch (error) {
        console.log(error);
      }
    },
    async GetUser() {
      try {
        await this.viewMe(this.id);
        this.form.username = this.user.username;
        this.form.full_name = this.user.full_name;
      } catch (error) {
        console.error(error);
        this.$router.push("/dashboard");
      }
    },
  },
};
</script>
