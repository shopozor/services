<template>
  <div>
    <h2 class="overview-title">
      {{ $t('budzons') }}
    </h2>
    <div class="p-6 text-justify">
      <p class="mb-5">
        Portugais Fribourgeois, je suis papa de deux enfants et un mari dévoué à sa famille ainsi qu''à la cause environnementale. Je me suis engagé dans
        ce projet dans l''optique de simplifier la transition de nos foyers vers une consommation plus écologique. Avec une interface qui sera agréable,
        autant sur le terrain que sur le web, la Budzonnerie permettra aux Consommateurs d''acheter des Produits locaux et respectueux de l''environnement
        tout en aidant le tissu économique local à se développer. Et ça, c''est mon engagement!
      </p>
      <p class="mb-5">
        Fribourgeois, petit-fils et neveu d''agriculteur, j''ai passé une grande partie de ma vie au contact du monde paysan. Boulanger-pâtissier de formation,
        j''aime les produits régionaux et de qualité. Je me suis engagé dans ce projet avec une pensée particulière pour les Producteurs. En effet, je veux leur
        permettre de produire et vendre de la qualité à un prix juste en faisant valoir leur travail, un prix qui leur permettra de vivre décemment. L''interface
        "Producteur" sera intuitive, simple d''utilisation, pour permettre aux Producteurs de consacrer leur temps à leurs marchandises. Avec cette plateforme,
        les Producteurs produisent seulement ce qui a été vendu, ce qui leur permet de réduire le gaspillage de leurs Produits.
      </p>
      <p class="mb-5">
        Co-fondateur fribourgeois de <a href="http://softozor.ch" target="_blank">softozor</a>, je suis aussi naturellement sensible à la cause défendue par Carlos et Rémi.
        Avec l''aide de mes associés Thomas, Cédric et Florian, ainsi que de mes coéquipiers Kilian et Nils, j''ai bien l''intention de mettre la technique au service de notre
        commerce de proximité. Notre équipe investit son temps libre pour trouver les solutions les plus pratiques et moins onéreuses possible, afin de produire elle aussi
        sa contribution artisanale pour sa région.
      </p>
      <p class="mb-5">
        <a href="http://www.softozor.ch" target="_blank">Softozor</a> est une entité qui regroupe des professionnels passionnés de programmation, d''enseignement et de jeux vidéos.
        Elle a été créée en juillet 2017 dans le but principal de s''amuser. Un but subsidiaire est de développer des logiciels d''apprentissage de toutes sortes. Dans le projet de
        la Budzonnerie, les motivations de Softozor sont multiples, entre autres : s''amuser dans le monde de l''e-commerce, agir en faveur du circuit court, former des développeurs
        aux applications web, obtenir une source de revenus pour financer ses propres projets de jeux vidéos.
      </p>
    </div>
    <img class="w-1/2 rounded-full mx-auto lg:max-w-lg" :src="budzons">
  </div>
</template>
<script>
import BudzonsImg from '~/assets/img/budzons.jpg'

export default {
  data: () => ({
    budzons: BudzonsImg
  })
}
</script>
