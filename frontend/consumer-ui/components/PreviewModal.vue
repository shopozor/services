<template>
  <div class="border-solid border-4 border-black h-full w-full overflow-auto">
    <div class="absolute top-0 left-0 text-black font-extrabold m-2 cursor-pointer" @click="onClose">
      &#10008;
    </div>
    <h1 class="font-extrabold text-4xl text-center">
      Avant-première
    </h1>
    <p class="p-4">
      Bienvenue sur l'avant-première de la Budzonnerie ! <span class="font-bold">Cette application est en construction.</span>
      Nous vous encourageons à la visiter régulièrement et nous faire un retour sur ce que vous en pensez au fur et à mesure de son développement. Si vous
      voyez par exemple des bugs, ou si vous pensez que votre expérience utilisateur pourrait être améliorée, n'hésitez pas à nous contacter. Nous adapterons
      notre <a href="https://github.com/shopozor/services/milestones?direction=asc&sort=due_date&state=open" target="_blank">roadmap</a> avec vos inputs.
    </p>
    <p class="p-4">
      Les informations sur la Budzonnerie qui sont présentées sur la page d'accueil sont réelles. Au contraire, les données sur les Budzonneries, leurs Produits et
      Producteurs sont complètement factices pour le moment. Avec le temps, nous remplacerons petit à petit ces données de démonstration avec celles correspondant
      à l'avancement de notre projet sur le terrain.
    </p>
  </div>
</template>

<script>
export default {
  methods: {
    onClose () {
      this.$emit('close')
    }
  }
}
</script>
