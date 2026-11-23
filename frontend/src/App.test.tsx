import { afterEach, describe, it, expect, vi } from "vitest";
import { screen } from "@testing-library/react";
import { renderWithProviders } from "@/test/render";
import App from "./App";

const renderApp = () => renderWithProviders(<App />);

afterEach(() => vi.unstubAllGlobals());

describe("App", () => {
  it("renders the placeholder heading", () => {
    vi.stubGlobal(
      "fetch",
      vi.fn(() => new Promise(() => {})),
    );
    renderApp();
    expect(screen.getByText("Enterprise Intellect")).toBeInTheDocument();
  });

  it("calls the same-origin ping endpoint and shows ok", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValue(
        new Response(JSON.stringify({ ok: true }), { status: 200 }),
      );
    vi.stubGlobal("fetch", fetchMock);
    renderApp();
    expect(await screen.findByText("API: ok")).toBeInTheDocument();
    expect(fetchMock).toHaveBeenCalledWith("/api/v1/ping");
  });

  it("shows an error when the API is unreachable", async () => {
    vi.stubGlobal("fetch", vi.fn().mockRejectedValue(new Error("down")));
    renderApp();
    expect(await screen.findByText("API: unreachable")).toBeInTheDocument();
  });
});
