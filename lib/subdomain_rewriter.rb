class SubdomainRewriter < Middleman::Extension
  def after_configuration
    app.use Middleware, middleman_app: app
  end

  # Middleware which rewrites links to directories into links to subdomains
  class Middleware
    def initialize(app, options={})
      @rack_app      = app
      @middleman_app = options[:middleman_app]
    end

    def call(env)
      status, headers, response = @rack_app.call(env)

      if @middleman_app.full_path(env['PATH_INFO']) =~ /(^\/$)|(\.(html|css|js)$)/
        body = ::Middleman::Util.extract_response_text(response)
        if body
          body = body.gsub(/((?:href|src|link)=[\'\"])\/(static|www|docs|update)\//) do |match|
            "#{$1}http://#{$2}.aegisub.org/"
          end
          return Rack::Response.new(body, status, headers).finish
        end
      end

      [status, headers, response]
    end
  end
end

::Middleman::Extensions.register(:subdomain_rewriter, SubdomainRewriter)
