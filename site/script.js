// Screenshot galleries: a thumb button swaps the main image.
for (const gallery of document.querySelectorAll("[data-gallery]")) {
  const link = gallery.querySelector(".shot");
  const image = link.querySelector("img");
  const buttons = gallery.querySelectorAll(".thumbs button");

  for (const button of buttons) {
    button.addEventListener("click", () => {
      image.src = button.dataset.src;
      image.alt = button.dataset.alt;
      link.href = button.dataset.src;
      for (const other of buttons) {
        other.setAttribute("aria-pressed", String(other === button));
      }
    });
  }
}

// Terminal panels: a thumb button shows one command's output.
for (const terminal of document.querySelectorAll("[data-terminal]")) {
  const buttons = terminal.querySelectorAll(".thumbs button");

  for (const button of buttons) {
    button.addEventListener("click", () => {
      for (const other of buttons) {
        const selected = other === button;
        other.setAttribute("aria-pressed", String(selected));
        document.getElementById(other.getAttribute("aria-controls")).hidden = !selected;
      }
    });
  }
}
