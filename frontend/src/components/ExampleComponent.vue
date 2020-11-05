<template>
  <div class="container">
    <p align="center">
      <img src="https://i.imgur.com/sCP3Ym9.png">
    </p>
    <input class="searchBtn">
    <button type="submit" class="submitBtn">Locuj mame ti ebem</button>
    <img src="https://i.imgur.com/KcWf8vQ.png" class="footer">
  </div>
</template>

<script>
export default {
  name: 'FirstComponent'
}
</script>

<style lang="scss" scoped>
  .searchBtn{
    position: absolute;
      top: 50%;
  left: 50%;
    transform: translate(-50%, -50%);
  }
    .submitBtnb{
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  }
  h1 {
    text-align: center;
  }
  .footer{
  left: 0;
  bottom: 0;
  width: 100%;
  text-align: center;
  }
</style>
