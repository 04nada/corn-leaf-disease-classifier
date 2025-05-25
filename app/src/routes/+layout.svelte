<script>
  let { children } = $props();
  const background_url = "https://i.pinimg.com/736x/4e/89/ee/4e89ee209dcf770ef411177dfb0bb940.jpg"
  import "../app.css";
</script>

<main style="min-height: 100vh; background-image:url('{background_url}'); background-size: cover; background-position: center;">
<div class="h-full w-full bg-emerald-700/40">
{@render children()}
</div>
</main>