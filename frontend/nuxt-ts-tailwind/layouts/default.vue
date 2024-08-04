<template class="size-full">
  <Sidebar :title>
    <template v-slot:navbar>
      <Navbar :title>
        <!-- <template v-slot:navbarfuntion>
          <slot name="innavbarfuntion"></slot>
        </template> -->
      </Navbar>
    </template>
    <template v-slot:sidebaritem>
      <SidebarItem :items="siderbaritems"></SidebarItem>
    </template>
    <slot></slot>
  </Sidebar>
</template>

<script lang="ts" setup>
const title = 'NLP in Map'

const book = Array.from({ length: 18 }, (_, index) => ({
  text: `Chapter ${index + 1}`,
  link: `/chapter/${index + 1}`
}));

const siderbaritems = [
  {
    text: 'Book',
    items: book
  },
  {
    text: 'Auth',
    items: [
      { text: 'User', link: '/user' },
      { text: 'Group', link: '/group' }
    ]
  }
]
</script>

<style>
.page-enter-active {
  transition: all 0.1s ease-out;
}

.page-leave-active {
  transition: all 0.1s ease-in;
}

.page-enter-from,
.page-leave-to {
  opacity: 0.2;
  filter: blur(1rem);
}
</style>