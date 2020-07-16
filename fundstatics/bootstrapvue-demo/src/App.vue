<template>
    <div id="app">
        <Navbar/>
        <router-view>
            <Index/>
        </router-view>


    </div>
</template>
<script>
    import Index from './components/Index.vue'
    import Navbar from './components/Navbar.vue';

    export default {
        name: 'navbar',
        components: {
            Navbar,
            Index
        }
    }
</script>