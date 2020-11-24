(ns clojure-katas.challenge-383
  (:require
   [clojure.tools.logging :as log]
   [clojure.string :as s]))

;; challenge
(defn same_necklace [str-a str-b]
  (if (= (count str-a) (count str-b))
      (let [str-b-double (str str-b str-b)]
        (s/includes? str-b-double str-a))
  false))
