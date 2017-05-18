class ScoresController < ApplicationController
  skip_before_filter :verify_authenticity_token

  def create
    selection = params[:selection]
    resp = Faraday.get 'https://www.instagram.com/theknot/media/'
    scores = `python score.py #{resp.body}` # => '1, .8, .5, 0'
    scores = scores.split(',')
    render json: scores
  end
end
