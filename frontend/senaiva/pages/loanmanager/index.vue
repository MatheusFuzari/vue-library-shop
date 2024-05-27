<script setup lang="ts">
import type { Loan } from "~/interfaces/loan";
import { getLoans } from "~/services/loanService";
definePageMeta({
  middleware: "auth",
});

const allLoans: Ref<Array<Loan>> = ref([]);


const handleLoans = () => {
  getLoans()
    .then(res => {
      console.log(res?.results);
      allLoans.value = res?.results ?? [];
      console.log(allLoans)
    })
    .catch(err => {
      console.error('error ', err);
    })
}
handleLoans();
</script>
<template>
  <div class='w-[40%] h-fit bg-slate-200 rounded-md m-auto mt-5 p-10'>
    <Toast />
    <div v-for="loan in allLoans">
      <LoanItem :loan="loan" v-if="loan.deliverDate == null" />
    </div>
  </div>
</template>