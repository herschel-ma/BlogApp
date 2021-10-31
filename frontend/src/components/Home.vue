<template>
  <!-- component -->
  <div class="overflow-x-hidden bg-gray-100">
    <div class="px-6 py-8">
      <div class="container flex justify-between mx-auto">
        <div class="w-full lg:w-8/12">
          <div class="flex items-center justify-between">
            <h1 class="text-xl font-bold text-gray-700 md:text-2xl">Post</h1>
            <div>
              <select
                class="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              >
                <option>Latest</option>
                <option>Last Week</option>
              </select>
            </div>
          </div>
          <div class="mt-6" v-for="article in articles" :key="article.id">
            <div class="max-w-4xl px-10 py-6 mx-auto bg-white rounded-lg shadow-md">
              <div class="flex items-center justify-between">
                <span class="font-light text-gray-600">{{ article.created_at }}</span>
                <a
                  href="#"
                  class="px-2 py-1 font-bold text-gray-100 bg-gray-600 rounded hover:bg-gray-500"
                >Laravel</a>
              </div>
              <div class="mt-2">
                <a
                  href="#"
                  class="text-2xl font-bold text-gray-700 hover:underline"
                >{{ article.title }}</a>
                <p class="mt-2 text-gray-600">{{ article.body }}</p>
              </div>
              <div class="flex items-center justify-between mt-4">
                <router-link
                  class="text-blue-500 hover:underline"
                  :to="{ name: 'details', params: { slug: article.slug } }"
                >Read more</router-link>
                <div>
                  <a href="#" class="flex items-center">
                    <img
                      src="https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=731&amp;q=80"
                      alt="avatar"
                      class="hidden object-cover w-10 h-10 mx-4 rounded-full sm:block"
                    />
                    <h1 class="font-bold text-gray-700 hover:underline">{{ article.author }}</h1>
                  </a>
                </div>
              </div>
            </div>
          </div>
          <!-- paganation -->
          <page-nation />
        </div>
        <div class="hidden w-4/12 -mx-8 lg:block">
          <!--Authors-->
          <Authors />
          <Category />
          <recent-post />
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>

import Cookies from 'js-cookie'
import axios from 'axios'
import PageNation from '@/components/PageNation'
import Authors from '@/components/Authors'
import Category from '@/components/Category'
import RecentPost from '@/components/RecentPost'
import Footer from '@/components/Footer'


export default {
  components: {
    PageNation,
    Authors,
    Category,
    RecentPost,
    Footer,
  },
  data() {
    return {
      articles: [],
      args: "yyy-mm-dd hh:mm:ss",
    }
  },
  methods: {
    getAllArticles() {
      axios.get('/api/articles/', {
        headers: {
          'Content-Type': "Application/json",
          'X-CSRFTOKEN': Cookies.get('csrftoken'),
          'Authorization': 'Token ' + localStorage.getItem('token')
        }
      })
        .then(response => response.data)
        .then(data =>
          this.articles.push(...data.map(a => {
            const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
            a.created_at = new Date(a.created_at).toLocaleDateString("en-US", options);
            a.body = a.body.slice(0, 100)
            return a
          }))
        )
        .catch(error => console.log(error))
    },
    getTokens() {
    }
  },
  mounted() {
    this.getAllArticles()
    this.getTokens()
  },
}
</script>

