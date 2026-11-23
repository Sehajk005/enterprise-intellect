import type { ReactElement } from "react";
import { render, type RenderOptions } from "@testing-library/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { MemoryRouter } from "react-router";

interface Options extends Omit<RenderOptions, "wrapper"> {
  /** Initial URL for the in-memory router. */
  route?: string;
}

/** Render with the same providers as main.tsx, using a fresh no-retry QueryClient per test. */
export function renderWithProviders(
  ui: ReactElement,
  { route = "/", ...options }: Options = {},
) {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });
  return {
    queryClient,
    ...render(ui, {
      wrapper: ({ children }) => (
        <QueryClientProvider client={queryClient}>
          <MemoryRouter initialEntries={[route]}>{children}</MemoryRouter>
        </QueryClientProvider>
      ),
      ...options,
    }),
  };
}
