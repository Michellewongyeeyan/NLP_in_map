<!-- https://leaflet.nuxtjs.org/ -->
<template>
  <div class="size-full">
    <LMap ref="map" :zoom="zoom" :center="[52.21322, -0.359482]" :use-global-leaflet="false" autoZIndex class="z-0">
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
    </LMap>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps<{
  datas: TChapterMap[]
}>()

const zoom = ref<number>(6)
</script>