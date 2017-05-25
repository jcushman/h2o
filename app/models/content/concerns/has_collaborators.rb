# Concerns relevant to any Node that can have collaborators
# - allows Child nodes to expose the same API as Casebooks, using the collaborator association defined by their Casebook
module Content::Concerns::HasCollaborators
  extend ActiveSupport::Concern

  included do
      has_many :users, class_name: 'User', through: :collaborators, source: :user, inverse_of: :collaborations
      has_many :owners, -> {where content_collaborators: {role: 'owner'}}, class_name: 'User', through: :collaborators, source: :user
      has_many :editors, -> {where content_collaborators: {role: 'editor'}}, class_name: 'User', through: :collaborators, source: :user
      has_many :reviewers, -> {where content_collaborators: {role: 'reviewer'}}, class_name: 'User', through: :collaborators, source: :user
  end
end