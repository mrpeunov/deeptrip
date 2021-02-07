<template>
<header>
  <div class="information">
    <div class="information_block">Лого</div>
    <div class="information_block">Ссылки</div>
    <div class="information_block">Разместить эскурсию</div>
  </div>
  <h1>Разместить экскурсию</h1>
  <h2>Без коммисий и предоплат</h2>
  <button>Карта экускурсий</button>
</header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
.information{
  display: flex;
}

header{
  background-image: url("../assets/background.png");
}
</style>
