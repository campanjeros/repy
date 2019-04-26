defmodule Metad.Mixfile do
  use Mix.Project

  def project do
    [
      app: :bla,
      version: "0.2.0",
      elixir: "~> 1.8",
      build_embedded: true,
      start_permanent: true,
      deps: deps(),
      test_coverage: [tool: ExCoveralls]
    ]
  end
end
