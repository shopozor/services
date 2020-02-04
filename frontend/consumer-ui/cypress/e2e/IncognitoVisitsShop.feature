# language: fr

Fonctionnalité: Incognito visite un Shop

  **En tant qu'Incognito,  
  je veux pouvoir entrer dans un Shop  
  pour voir quels Produits il propose et faire connaissance avec ses Producteurs.**  

  Entrer dans un Shop ne nécessite pas de compte. Un compte rend juste l'utilisation du Shopozor plus confortable.
  Les prix des Produits sont montrés de façon transparente : les catalogues montrent clairement les prix brut et net
  de chaque Produit et de chaque Format de Produit, ainsi que les taxes correspondantes. Voir
  [issue "Take Swiss VAT into account"](https://github.com/shopozor/backend/issues/95) pour plus de détails sur comment
  toutes ces valeurs sont calculées.

  Contexte: L'utilisateur est Incognito

    Etant donné un utilisateur non identifié

  Scénario: Incognito choisit un Shop

    Etant donné qu'Incognito se trouve sur la page d'accueil
    # We need to make a snapshot image test here to ensure that we really see a map
    Alors il voit la carte des Shops
    Lorsqu'il clique sur un Shop
    # Here we need to check that the selected Shop has the properties stored in the DB
    Alors il voit les caractéristiques de ce Shop
    # Here we need to check that the Shop card has a link to the Shop
    Et il peut entrer dedans

  @wip
  Scénario: Incognito se balade dans les Rayons d'un Shop

    Incognito peut entrer dans un Shop pour y consulter son catalogue de Produits. Celui-ci
    exhibe les Produits avec leur Producteur et montre sous quels Formats chaque Produit
    est disponible avec leurs prix. Pour éviter de noyer Incognito dans trop d'information,
    la visite d'un Shop se fait au travers des différents Rayons qu'il propose. Chaque Shop propose
    les mêmes Rayons mais les remplit avec des Produits différents réalisés par des Producteurs différents.
    Il n'est par exemple pas possible à Incognito de se procurer le catalogue complet du Shop d'un seul coup.
    Au lieu de cela, il peut en obtenir le catalogue de la boulangerie, de la fromagerie, de la boucherie, etc.

    Etant donné qu'Incognito a choisi un Shop
    # Confront to DB
    Alors il peut en voir les Rayons
    Lorsqu'il se balade dans l'un de ces Rayons
    # Confront to DB
    Alors il voit les Produits correspondants avec leurs stocks et leurs prix
    Lorsqu'il inspecte l'un de ces Produits
    # Confront to DB
    Alors il voit les détails du Produit

