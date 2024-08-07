<!-- https://leaflet.nuxtjs.org/ -->
<template>
  <div class="size-full">
    <LMap ref="map" :zoom="zoom" :center="[54.74322, -2.59482]" :use-global-leaflet="false" autoZIndex class="z-0">
      <LTileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&amp;copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors"
        layer-type="base" name="OpenStreetMap" />
      <LMarker :lat-lng="data.nominatim" draggable v-for="data, index in props.datas" :key="index">
        <LPopup>{{ data.location }}
          <br>
          <div v-for="txt, textIndex in data.text">
            <p><b>{{ textIndex + 1 }}.</b> {{ txt }}</p>
          </div>
        </LPopup>
      </LMarker>

      <LRectangle :lat-lngs="[
        [49.934852, -11.909485],
        [58.742596, 2.700568]
      ]" :fill="false" color="#35495d">
    </LRectangle>
    </LMap>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps<{
  datas: TChapterMap[]
}>()

const zoom = ref<number>(6)
</script>