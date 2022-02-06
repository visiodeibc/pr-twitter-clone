import axios from 'axios';

const state = {
  tweets: null,
  tweet: null
};

const getters = {
  stateTweets: state => state.tweets,
  stateTweet: state => state.tweet,
};

const actions = {
  async createTweet({dispatch}, tweet) {
    await axios.post('tweets', tweet);
    await dispatch('getTweets');
  },
  async getTweets({commit}) {
    let {data} = await axios.get('tweets');
    commit('setTweets', data);
  },
  async viewTweet({commit}, id) {
    let {data} = await axios.get(`tweet/${id}`);
    commit('setTweet', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateTweet({}, tweet) {
    await axios.patch(`tweet/${tweet.id}`, tweet.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteTweet({}, id) {
    await axios.delete(`tweet/${id}`);
  }
};

const mutations = {
  setTweets(state, tweets){
    state.tweets = tweets;
  },
  setTweet(state, tweet){
    state.tweet = tweet;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};