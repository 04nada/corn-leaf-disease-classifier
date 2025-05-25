<script lang="ts">

    import { onMount } from 'svelte';
    let message = "";
    let imageUrl = "";
    let fileInput: any;
    let modelType = "cnn"; 
    
    const HOST = "http://localhost:8000"

    function handleFileChange(event) {
        const file = event.target.files[0];
        if (file) {
            imageUrl = URL.createObjectURL(file);
        } else {
            imageUrl = "";
        }
    }

    async function handleClassify() {
        const file = fileInput.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        const endpoint = modelType === "cnn"
            ? `${HOST}/cnn-classify`
            : `${HOST}/svm-classify`;

        const res = await fetch(endpoint, {
            method: "POST",
            body: formData
        });

        const data = await res.json();
        message = data.result;
    }

    onMount(async () => {
        const res = await fetch(`${HOST}/`, { method: "GET" });
        const data = await res.json();
        console.log(data.message)
    });
</script>

<div class="min-h-screen bg-cover bg-center flex items-center justify-center px-4">
  <div class="bg-white h-full border border-gray-300/50
    bg-opacity-90 backdrop-blur-md rounded-2xl shadow-xl p-8 max-w-4xl w-full grid grid-cols-1 md:grid-cols-2 gap-8">

    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <div>
      <h1 class="text-2xl font-bold text-green-800 mb-4">Corn Leaf Disease Classification</h1>
      <p class="text-gray-700 mb-6">Upload an image of a corn leaf to classify its disease.</p>

      <div class="mb-4 flex gap-4 justify-center">
        <label>
          <input type="radio" name="model" value="cnn" bind:group={modelType} checked />
          <span class="ml-1">CNN</span>
        </label>
        <label>
          <input type="radio" name="model" value="svm" bind:group={modelType} />
          <span class="ml-1">SVM</span>
        </label>
      </div>

      <!-- svelte-ignore a11y_no_static_element_interactions -->
      <div
        class="border-2 border-dashed border-gray-300 rounded-lg p-6 mb-4 text-center cursor-pointer"
        on:click={() => fileInput.click()}
      >
        <input
          type="file"
          accept="image/*"
          bind:this={fileInput}
          on:change={handleFileChange}
          class="hidden"
        />
        {#if imageUrl}
          <img src={imageUrl} alt="Preview" class="mx-auto max-h-40 rounded mt-2" />
        {/if}
        <div class="text-gray-500 mt-2">{!imageUrl ? "Choose an image" : ""}</div>
      </div>

      <button
        class="w-full bg-green-700 text-white font-semibold py-2 rounded-lg hover:bg-green-800 transition"
        on:click={handleClassify}
      >
        Classify
      </button>
    </div>

    <div class="bg-green-50 p-6 rounded-lg">
      <h2 class="text-xl font-bold text-green-800 mb-2">Result</h2>
      <p class="text-gray-700">Disease:</p>
      <p class="text-2xl font-semibold text-green-900">{message}</p>
    </div>
  </div>
</div>