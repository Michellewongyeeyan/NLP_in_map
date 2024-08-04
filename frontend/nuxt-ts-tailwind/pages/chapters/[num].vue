<template>
    <Map :datas="datas"></Map>
</template>

<script setup lang="ts">
import { getsChapterByNum } from '~/utils/db/mongo/chapter'
const route = useRoute()
const datas = ref<TchapterMap[]>([])

onMounted( async () => {
    const res = ((await getsChapterByNum(route.params.num)).data)
    datas.value = res.filter( e => e.nominatim.length !== 0)
})
</script>