<template>
    <div id="app">
        <router-view>
            <Index/>
        </router-view>
    </div>
</template>
<script>
    import Index from './components/Index.vue'
    export default {
        name: 'navbar',
        components: {
            Index
        }
    }
</script>