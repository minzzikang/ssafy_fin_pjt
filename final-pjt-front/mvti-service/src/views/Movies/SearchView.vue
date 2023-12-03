<template>
    <div class="d-flex">
        <Navbar />
        <div class="search-box">
            <h3 style="color: #f5f5f5;">영화 검색</h3>
            <SearchList />
        </div>
    </div>
</template>

<script setup>
import SearchList from '@/components/Movies/SearchList.vue'
import Navbar from '@/components/Movies/Navbar.vue'
</script>

<style scoped>
.search-box {
    flex: 1;
}
</style>