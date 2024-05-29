<script setup lang="ts">
const toggleChat:Ref<boolean> = ref(false);
const handleChat = () => {
  toggleChat.value = !toggleChat.value;
  console.log(toggleChat)
}
</script>
<template>
  <div>
    <Header />
    <slot></slot>
    <div class="fixed left-5 bottom-5">
      <Button :icon="toggleChat ? 'pi pi-times' : 'pi pi-comment'" :label="toggleChat ? 'Fechar' : 'Chatbot'" @click="handleChat" class='bg-green-500 p-3 px-5'/>
      <div v-if="toggleChat">
        <iframe allow="microphone;" width="350" height="430"
          src="https://console.dialogflow.com/api-client/demo/embedded/de20e637-5ba8-4d89-8637-18dcd2fd3de1">
        </iframe>

      </div>
    </div>
  </div>
</template>